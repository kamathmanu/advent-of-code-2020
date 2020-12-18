#include <algorithm>
#include <fstream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;

std::vector<int>
parse(std::ifstream &&input) { // why must input be a forwarded type??
  return rs::getlines(input) |
         rv::transform([](auto &&s) { return std::stoi(s); }) |
         rs::to<std::vector>;
}

auto accumulate_multiply(const std::vector<int> &v) {
  return rs::accumulate(v, 1, std::multiplies());
}

std::vector<int> two_sum(const std::vector<int> &nums) {
  std::unordered_set<int> seen;
  const auto target_year = 2020;
  for (const auto &num : nums) {
    const auto complement = target_year - num;
    if (seen.count(complement)) {
      return {complement, num};
    } else {
      seen.insert(num);
    }
  }
  return {}; // technically this should not be an issue.
}

std::vector<int> three_sum(std::vector<int> &nums) {
  // fix each number and conduct two sum for that num,
  // taking advantage of two pointers since we've sorted everything.
  rs::sort(nums);
  const auto N = nums.size();
  for (size_t i = 0; i < N; i++) {
    if (i > 0 && nums[i] == nums[i - 1]) {
      continue;
    }

    auto left = i + i, right = N - 1;
    while (left <= right) {
      const auto target = nums[i] + nums[left] + nums[right];
      if (target < 2020) {
        left++;
      } else if (target > 2020) {
        right--;
      } else {
        return {nums[i], nums[left], nums[right]};
      }
    }
  }
  return {};
}

int part1(const std::vector<int> &nums) {
  return accumulate_multiply(two_sum(nums));
}

int part2(std::vector<int> &nums) {
  return accumulate_multiply(three_sum(nums));
}

int main(int argc, char const *argv[]) {
  // std::ifstream in("input.txt", std::ios::in);
  std::vector<int> input =
      parse(std::ifstream{"../../input.txt", std::ios::in});
  fmt::print("Part 1: {}\n", part1(input));
  fmt::print("Part 2: {}\n", part2(input));
  return 0;
}
