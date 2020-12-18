#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include <fmt/core.h>
#include <fmt/ranges.h>
#include <range/v3/all.hpp>

namespace rs = ranges;
namespace rv = ranges::views;

std::vector<long> parse_input(std::istream &&input) {
  return rs::getlines(input) |
         rv::transform([](auto &&s) { return std::stol(s); }) |
         rs::to<std::vector>;
}

auto sum_exists = [](const std::vector<long> &input, size_t preamble_low,
                     size_t preamble_high) {
  const auto &target = input[preamble_high + 1];
  // loop over the preamble range
  for (auto i = preamble_low; i < preamble_high; ++i) {
    for (auto j = i + 1; j <= preamble_high; ++j) {
      if ((input[i] + input[j] == target)) {
        return true;
      }
    }
  }
  return false;
};

long part1(const std::vector<long> &nums, const size_t &preamble_size) {

  size_t i = 0, j = preamble_size - 1, N = nums.size();
  // find an algo to replace this
  while (j < N - 1) {
    if (!sum_exists(nums, i, j)) {
      return nums[j + 1];
    }
    i++;
    j++;
  }
  return static_cast<long>(0);
}

long part2_brute_force(const std::vector<long> &nums,
                       const long &invalid_number) {
  size_t i = 0, j = 2;
  size_t top_range = 2;
  const auto N = nums.size();
  while (top_range < N) {
    if (j >= N) {
      top_range++;
      i = 0;
      j = top_range;
    }
    std::vector<long> subset(std::next(nums.begin(), i),
                             std::next(nums.begin(), j + 1));
    const auto subset_sum = std::accumulate(subset.begin(), subset.end(), 0);
    if (subset_sum == invalid_number) {
      // sort and return the sum of lowest and highest
      std::sort(subset.begin(), subset.end());
      return subset.front() + subset.back();
    }
    i++;
    j++;
  }

  return static_cast<long>(0);
}

// This is (tehnically) DP? - optimized two pointer approach.
long part2(const std::vector<long> &nums, const long &invalid_number) {
  assert(nums.size() >
         1); // technically, it should be at least preamble length + 1...
  // using iterators might be better style than indexing...
  auto left = std::begin(nums), right = std::begin(nums) + 1;

  long sum = *left + *right;

  while (right != std::end(nums)) {
    if (sum < invalid_number) {
      ++right;
      sum += *right;
    } else if (sum > invalid_number) {
      sum -= *left;
      ++left;
    } else {
      break;
    }
  }
  // we're assured that there is an invalid number
  // a nice case where we should consider: do we wish to sort? or is it just
  // enough to conduct 2 linear passes to get the max and min element?
  const auto min =
      std::accumulate(left, right, LONG_MAX, [](const auto &a, const auto &b) {
        return std::min(a, b);
      });
  const auto max =
      std::accumulate(left, right, LONG_MIN, [](const auto &a, const auto &b) {
        return std::max(a, b);
      });
  return min + max;
}

int main() {
  // std::ifstream in("input.txt", std::ios::in);
  std::vector<long> cipher_nums =
      parse_input(std::ifstream{"../../input.txt", std::ios::in});

  const auto invalid_number = part1(cipher_nums, 25);
  fmt::print("Part 1: {}\n", invalid_number); // 248131121
  std::vector<long> test_nums = {35,  20,  15,  25,  47,  40,  62,
                                 55,  65,  95,  102, 117, 150, 182,
                                 127, 219, 299, 277, 309, 576};
  fmt::print("Part 2: {}\n", part2(cipher_nums, invalid_number));

  return 0;
}