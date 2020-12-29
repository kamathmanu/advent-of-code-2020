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

std::vector<std::string> parse(std::istream &&input) {
  std::stringstream strStream;
  strStream << input.rdbuf();
  std::string s = strStream.str();
  return s | rv::split("\n") | ranges::to<std::vector<std::string>>();
  //   return rs::getlines(input) | rv::transform([](auto &&s) {
  //            rs::sort(s);
  //            return s;
  //          }) |
  //          ranges::to<std::vector>;
}

// int64_t part1(const std::vector<std::string> &input) {
//   auto rng =
//       input | rv::split("") | rv::transform([](auto &&rng) { auto first = })
// }

int main() {
  auto input = parse(std::ifstream{"../../input.txt", std::ios::in});
  fmt::print("{}\n", input[0]);
  //   fmt::print("Part 1 Solution: {}\n", part1(input));
  //   fmt::print("Part 2 Solution: {}\n", part2(input));

  return 0;
}