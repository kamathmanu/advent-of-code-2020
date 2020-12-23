#include <bitset>
#include <fstream>
#include <map>
#include <regex>
#include <stdexcept>
#include <string>

#include "range/v3/all.hpp"
#include <fmt/core.h>
#include <fmt/ranges.h>

namespace rs = ranges;
namespace rv = ranges::views;
using map = std::map<unsigned long long, unsigned long long>;

std::string value_as_bits(const std::string &val) {
  static constexpr size_t bit_length = 36;
  return std::bitset<bit_length>{
      static_cast<unsigned long long>(std::stoull(val))}
      .to_string();
}

unsigned long long apply_mask(const std::string &mask,
                              const std::string &value) {
  auto result = rv::zip(value, mask) | rv::transform([](auto &&p) {
                  return p.second == 'X' ? p.first : p.second;
                }) |
                rs::to<std::string>;
  return std::stoull(result, nullptr, 2);
}

// revisit this for for algo practice.
std::vector<unsigned long long> version2_decode(const std::string &mask,
                                                const std::string &addr) {
  auto bitmask_result = rv::zip(addr, mask) | rv::transform([](auto &&p) {
                          return p.second == '0' ? p.first : p.second;
                        }) |
                        rs::to<std::string>;

  std::vector<std::string> floating_addr{bitmask_result};

  while (rs::find_if(floating_addr, [](const auto &s) {
           return rs::contains(s, 'X');
         }) != rs::end(floating_addr)) {

    std::vector<std::string> tmp;
    for (auto s : floating_addr) {
      auto pos = s.find_first_of('X');
      if (pos != std::string::npos) {
        s[pos] = '0';
        tmp.push_back(s);
        s[pos] = '1';
        tmp.push_back(s);
      } else {
        tmp.push_back(s);
      }
    }
    std::swap(floating_addr, tmp);
  }
  return floating_addr |
         rv::transform([](auto &&s) { return std::stoull(s, nullptr, 2); }) |
         rs::to<std::vector<unsigned long long>>;
}

unsigned long long part1(std::istream &&input) {
  std::string tmp;
  std::smatch m;

  map memory_addresses;
  std::string mask;

  while (std::getline(input, tmp)) {
    if (tmp.substr(0, 4) == "mask") {
      mask = tmp.substr(7);
    } else {
      if (!std::regex_match(tmp, m, std::regex{R"(mem\[(\d+)\] = (\d+))"})) {
        throw std::runtime_error{"Invalid input received"};
      }
      auto idx = std::stoull(m.str(1));
      auto num = apply_mask(mask, value_as_bits(m.str(2)));
      memory_addresses[idx] = num;
    }
  }
  return rs::accumulate(memory_addresses | rv::values, 0UL);
}

unsigned long long part2(std::istream &&input) {
  std::string tmp;
  std::smatch m;

  map memory_addresses;
  std::string mask;

  while (std::getline(input, tmp)) {
    if (tmp.substr(0, 4) == "mask") {
      mask = tmp.substr(7);
    } else {
      if (!std::regex_match(tmp, m, std::regex{R"(mem\[(\d+)\] = (\d+))"})) {
        throw std::runtime_error{"Invalid input received"};
      }

      auto addresses = version2_decode(mask, value_as_bits(m.str(1)));
      for (auto address : addresses) {
        memory_addresses[address] = std::stoull(m.str(2));
      }
    }
  }
  return rs::accumulate(memory_addresses | rv::values, 0UL);
}

int main() {
  // used inspiration from
  // https://github.com/apathyboy/aoc2020cpp/blob/master/days/day14/main.cpp
  const std::string input_path = "../../input.txt";

  fmt::print("Part 1: {}\n", part1(std::ifstream{input_path}));
  fmt::print("Part 2: {}\n", part2(std::ifstream{input_path}));
}