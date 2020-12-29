#include <algorithm>
#include <fstream>
#include <string>
#include <tuple>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;

std::vector<std::string> parse(std::istream &&input) {
  return rs::getlines(input) | rs::to_vector;
}

// non-algorithmic raw-loops solution: good start
auto part1_raw(const std::vector<std::string> &pattern,
               const std::pair<int, int> &slope) {

  auto down = 0, right = 0, trees = 0;
  while (down < pattern.size()) {
    if (pattern[down][right % pattern[down].size()] == '#') {
      trees++;
    }
    down += slope.first;
    right += slope.second;
  }
  return trees;
}

auto part1(std::vector<std::string> pattern, const std::pair<int, int> &slope) {
  const int M = pattern.size(); // iota needs to take ints??
  return rs::count_if(rv::iota(0, M) | rv::stride(slope.first), [&](int row) {
    const auto col = row * slope.second / slope.first;
    return pattern[row][col % pattern[row].size()] == '#';
  });
}

long part2(const std::vector<std::string> &pattern,
           const std::vector<std::pair<int, int>> &slopes) {
  return rs::accumulate(slopes | rv::transform([&](const auto &slope) {
                          return part1(pattern, slope);
                        }),
                        1L, std::multiplies());
}

int main() {
  auto input = parse(std::ifstream{"../../input.txt", std::ios::in});
  const std::vector<std::pair<int, int>> slopes = {
      std::make_pair(1, 1), std::make_pair(1, 3), std::make_pair(1, 5),
      std::make_pair(1, 7), std::make_pair(2, 1)};
  fmt::print("Part 1: {}\n", part1(input, slopes[1]));
  fmt::print("Part 2: {}\n", part2(input, slopes));
  return 0;
}