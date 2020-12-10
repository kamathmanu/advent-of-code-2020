#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

auto sum_exists = [](const std::vector<uint32_t> &input, size_t preamble_low,
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

uint32_t part1(const std::vector<uint32_t> &nums, const size_t &preamble_size) {

  size_t i = 0, j = preamble_size - 1, N = nums.size();
  while (j < N - 1) {
    if (!sum_exists(nums, i, j)) {
      return nums[j + 1];
    }
    i++;
    j++;
  }
  return 0;
}

uint32_t part2(const std::vector<uint32_t> &nums,
               const uint32_t &invalid_number) {
  size_t i = 0, j = 2;
  size_t top_range = 2;
  const auto N = nums.size();
  while (top_range < N) {
    if (j >= N) {
      top_range++;
      i = 0;
      j = top_range;
    }
    std::vector<uint32_t> subset(std::next(nums.begin(), i),
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

  return 0;
}

int main() {
  // generate a vector of values from a file
  std::vector<uint32_t> cipher_nums;
  std::ifstream input("input.txt", std::ios::in);
  if (input.is_open()) {
    std::string line;
    while (getline(input, line)) {
      cipher_nums.push_back(std::stoul(line));
    }
    input.close();
  }

  const auto invalid_number = part1(cipher_nums, 25);
  std::cout << "Part 1: " << invalid_number << "\n"; // 248131121
  std::cout << "Part 2: " << part2(cipher_nums, invalid_number) << "\n";

  return 0;
}
