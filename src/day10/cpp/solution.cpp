#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;

std::vector<int> parse(std::istream &&input) {
  return rs::getlines(input) |
         rv::transform([](auto &&s) { return std::stoi(s); }) |
         rs::to<std::vector>;
}

// since the jolt differences are homogeneous,
// we prefer std::array over std::tuple.
std::array<int, 3>
find_jolt_differences(const std::vector<int> &adapter_jolts) {
  std::array<int, 3> differences = {0, 0, 0};

  auto prev_jolt = 0; // NOTE: this is potentially an ITM anti-pattern.

  for (const auto &jolt : adapter_jolts) {
    // whenever dealing with comparing adjacent_elements, you should refer to
    // one of the adjacent_* or is_*_until algorithms!
    const auto potential_difference = jolt - std::exchange(prev_jolt, jolt);
    differences[potential_difference - 1]++;
  }

  // finally, add the phone's joltage as well
  differences[2]++;

  assert(std::accumulate(differences.begin(), differences.end(), 0) ==
         adapter_jolts.size() + 1);

  return differences;
}

void part1(const std::vector<int> &chain) {
  const auto differences = find_jolt_differences(chain);
  const auto answer = differences[0] * differences[2];
  fmt::print("Part 1: {}\n", answer);
}

// dynamic programming!
void part2(const std::vector<int> &chain) {

  // using an unordered_map, we don't need to explicitly handle corner cases
  // when i < 3. Interesting, revisit to see if you can use a vector?
  std::unordered_map<int, size_t> permutations{{0, 1}};

  for (const auto &jolt : chain) {
    permutations[jolt] += permutations[jolt - 1] + permutations[jolt - 2] +
                          permutations[jolt - 3];
  }
  fmt::print("Part 2: {}\n", permutations[chain.back()]);
}

int main() {
  std::vector<int> data = parse(std::ifstream{"../../input.txt", std::ios::in});
  rs::sort(data); // we're considering adapters from 0 jolts.
  part1(data);
  std::vector<int> test_data = {1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19};
  part2(data);

  return 0;
}