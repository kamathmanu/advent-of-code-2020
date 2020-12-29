#include <fstream>
#include <istream>
#include <sstream>
#include <string>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;
namespace ra = ranges::actions;

std::vector<std::string> parse(std::istream &&input) {
  return rs::getlines(input) | rv::transform([](auto &&s) {
           rs::sort(s);
           return s;
         }) |
         ranges::to<std::vector>;
}

int64_t part1(const std::vector<std::string> &input) {
  // https://www.fluentcpp.com/2020/04/03/implementing-a-line-filter-by-using-cpp-ranges/
  // clang-format off
    auto rng = input 
        | rv::split("") // newline characters separate groups
        | rv::transform([](auto&& group) { // map each group by concatenating the answers and then getting the unique sorted alphabets
            return rs::distance(group | rv::join | rs::to<std::vector> | ra::sort | ra::unique); });
  // clang-format on

  return rs::accumulate(rng, int64_t{0});
}

int64_t part2(const std::vector<std::string> &input) {
  // clang-format off
    auto rng = input 
        | rv::split("")
        | rv::transform([](auto&& rng) {
            auto first = rs::front(rng) | rs::to<std::vector>; // the common answer would be in the front

            for (auto s : rv::tail(rng)) { // front and tail are like car and cdr, neat!
                first = rv::set_intersection(first, s) | rs::to<std::vector>; // repeatedly find the intersection. 
            }

            return rs::distance(first); }); // and finally get the number of common answers.
  // clang-format on

  return rs::accumulate(rng, int64_t{0});
}

int main() {
  auto input = parse(std::ifstream{"../../input.txt", std::ios::in});
  fmt::print("Part 1 Solution: {}\n", part1(input));
  fmt::print("Part 2 Solution: {}\n", part2(input));

  return 0;
}