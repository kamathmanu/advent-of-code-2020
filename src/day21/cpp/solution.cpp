#include <fstream>
#include <map>
#include <regex>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;
namespace ra = ranges::actions;

struct food {
  std::vector<std::string> ingredients;
  std::vector<std::string> allergens;
};

std::vector<food> get(std::istream &&input) {
  return rs::getlines(input) | rv::transform([](auto &&line) {
           std::smatch m;
           if (!std::regex_match(line, m,
                                 std::regex(R"((.*)\(contains (.*)\))"))) {
             throw std::runtime_error("Unable to parse: invalid input\n");
           }
           // auto &[tmp_ingredients, tmp_allergens] = m.str();
           auto tmp_ingredients = m.str(1);
           auto tmp_allergens = m.str(2);

           food f;
           f.ingredients = tmp_ingredients | rv::split(' ') |
                           rv::transform([](auto &&token) {
                             return token | rs::to<std::string>;
                           }) |
                           rs::to_vector | ra::sort;

           f.allergens =
               tmp_allergens | rv::split(',') | rv::transform([](auto &&token) {
                 return token | rs::to<std::string>;
               }) |
               rv::transform([](auto &&s) {
                 return s |
                        rv::trim([](uint8_t c) { return std::isspace(c); }) |
                        rs::to<std::string>;
               }) |
               rs::to_vector | ra::sort;
           return f;
         }) |
         rs::to_vector;
}

std::vector<food> find_foods_with_allergen(const std::vector<food> &food_list,
                                           std::string_view allergen) {
  return food_list | rv::filter([&allergen](const auto &&f) {
           return rs::contains(f.allergens, allergen);
         }) |
         rs::to_vector;
}

// revisit
auto build_allergen_set(const std::vector<food> &food_list) {
  std::map<std::string, std::set<std::string>> allergen_potentials;

  for (auto &check_food : food_list) {
    for (auto allergen : check_food.allergens) {
      auto food_with_allergen = find_foods_with_allergen(food_list, allergen);
      auto potentials = check_food.ingredients;

      for (const auto &allergen_food : food_with_allergen) {
        potentials =
            rv::set_intersection(potentials, allergen_food.ingredients) |
            rs::to_vector;
      }

      for (auto p : potentials) {
        allergen_potentials[allergen].insert(p);
      }
    }
  }

  for (auto &allergen : allergen_potentials) {
    for (auto &test_allergen : allergen_potentials) {
      if (test_allergen.first == allergen.first)
        continue;
      if (allergen.second.size() == 1)
        break;
      allergen.second =
          rv::set_difference(allergen.second, test_allergen.second) |
          rs::to<std::set<std::string>>;
    }
  }

  return allergen_potentials |
         rv::transform([](auto &&p) { return rs::front(p.second); }) |
         rs::to_vector;
}

int64_t count_non_allergenic_ingredients(
    const std::vector<food> &food_list,
    const std::vector<std::string> &with_allergens) {
  auto all_ingredients = food_list |
                         rv::transform([](auto &&f) { return f.ingredients; }) |
                         ra::join;
  auto no_allergens =
      all_ingredients | rv::filter([&with_allergens](auto &&i) {
        return rs::none_of(with_allergens, [&i](auto ai) { return ai == i; });
      });

  return rs::distance(no_allergens);
}

int64_t part1(std::vector<food> food_list) {
  return count_non_allergenic_ingredients(food_list,
                                          build_allergen_set(food_list));
}

int main() {
  auto foods = get(std::ifstream{"../../input.txt"});
  fmt::print("Part 1: {}\n", part1(foods));
  return 0;
}