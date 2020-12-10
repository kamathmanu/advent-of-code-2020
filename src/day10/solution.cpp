#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

#include "../../common/common.hpp"

// since the jolt differences are homogeneous, we prefer std::array over
// std::tuple
std::array<uint32_t, 3> find_jolt_differences(const std::vector<uint32_t> &v) {
  std::array<uint32_t, 3> differences = {0, 0, 0};
  // std::accumulate?? we're reducing the vector into a triplet

  //   print_container(v, 5);

  auto prev_jolt = 0;
  for (const auto &num : v) {
    const auto joltage = (num - prev_jolt);
    switch (joltage) {
    case 1:
      differences[0]++;
      break;

    case 2:
      differences[1]++;
      break;

    case 3:
      differences[2]++;
      break;
    }
    prev_jolt = num;
  }

  // finally, add the phone's joltage as well
  differences[2]++;

  assert(std::accumulate(differences.begin(), differences.end(), 0) ==
         v.size() + 1);

  return differences;
}

void part1(std::vector<uint32_t> chain) {

  std::sort(chain.begin(), chain.end()); // since we go from 0 to
  const auto differences = find_jolt_differences(chain);
  const auto answer = differences[0] * differences[2];
  std::cout << "Part 1: " << answer << "\n";
}

int main(int argc, char const *argv[]) {
  // generate a vector of values from a file
  std::vector<uint32_t> data;
  std::ifstream input("input.txt", std::ios::in);
  if (input.is_open()) {
    std::string line;
    while (getline(input, line)) {
      data.push_back(std::stoul(line));
    }
    input.close();
  }

  part1(data);

  return 0;
}
