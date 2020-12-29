#include <algorithm>
#include <fstream>
#include <string>
#include <tuple>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;

std::tuple<int, int, char, std::string> get_tokens(const std::string &line) {
  auto tokens = line | rv::split(' ') | rs::to<std::vector<std::string>>();
  auto nums = tokens[0] | rv::split('-') | rs::to<std::vector<std::string>>();
  return std::make_tuple(std::stoi(nums[0]), std::stoi(nums[1]), tokens[1][0],
                         tokens.back());
}

std::vector<std::string> parse(std::istream &&input) {
  return rs::getlines(input) | rs::to_vector;
}

auto part1(const std::vector<std::string> &input) {
  return rs::count_if(input, [](const auto &line) {
    auto [lower, upper, ch, password] = get_tokens(line);
    auto freq = rs::count(password, ch);
    return freq >= lower && freq <= upper;
  });
}

auto part2(const std::vector<std::string> &input) {
  return rs::count_if(input, [](const auto &line) {
    auto [pos_a, pos_b, ch, password] = get_tokens(line);
    return (password[pos_a - 1] == ch) ^ (password[pos_b - 1] == ch);
  });
}

int main() {
  auto input = parse(std::ifstream{"../../input.txt", std::ios::in});
  fmt::print("Part 1: {}\n", part1(input));
  fmt::print("Part 2: {}\n", part2(input));
  return 0;
}