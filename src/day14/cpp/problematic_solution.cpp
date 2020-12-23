#include <fstream>
#include <memory>
#include <numeric>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

#include "range/v3/all.hpp"
#include <fmt/core.h>
#include <fmt/ranges.h>

namespace rs = ranges;
namespace rv = ranges::views;
using map = std::unordered_map<unsigned long, unsigned long>;

https : // www.fluentcpp.com/2017/04/21/how-to-split-a-string-in-c/
        std::vector<std::string>
        split(const std::string &s, char delimiter = ' ');

// Parses input as a program consisting of subsections,
// which are strings of program lines containing a mask,
// followed by the memory addresses to write to.
// Sections are delimited by masks.
std::vector<std::string> parse(std::istream &&input) {
  std::vector<std::string> lines = rs::getlines(input) | rs::to<std::vector>;

  // gotta be a neater way to do this
  auto group_into_sections = [&lines]() {
    std::string section = lines[0] + "\n";
    std::vector<std::string> program;
    for (auto it = lines.begin() + 1; it != lines.end(); ++it) {
      const auto line = *it + "\n";
      if (line.substr(0, 4) == "mask") {
        section.pop_back(); // get rid of newline character
        program.push_back(section);
        section = line;
      } else {
        section += line;
        if (it == std::prev(lines.end())) {
          section.pop_back();
          program.push_back(section);
        }
      }
    }
    return program;
  };
  auto program = group_into_sections();
  //   fmt::print("{}\n", program);
  return program;
}

std::vector<std::string> split(const std::string &s, char delimiter) {
  std::vector<std::string> tokens;
  std::string token;
  std::istringstream token_stream(s);
  while (std::getline(token_stream, token, delimiter)) {
    tokens.push_back(token);
  }

  return tokens;
}

std::vector<std::string> splitlines(const std::string &s) {
  return split(s, '\n');
}

// Extracts relevant info from a given module.
// Namely, we get the mask, and we also get the
// memory address - value pairs, which are stored
// as a smaller hash map (which usually contains 4-5 elements).
// std::pair<std::string, std::unordered_map<unsigned long, unsigned long>>
void parse_module(const std::string &module) {
  auto lines = splitlines(module);
  auto mask = lines[0].substr(7);
  fmt::print("{}\n", mask);
  map section_addresses;
  std::for_each(lines.begin() + 1, lines.end(), [](auto &line) {

  })
  // return std::make_pair("", {{}});
}

// unsigned long apply_mask(unsigned long value) { return 0UL; }

void update_address(std::string &module, map &memory_addresses) {

  // auto [mask, addr_value_pairs] = parse_module(module);
  parse_module(module);
  // for (const auto &address : addr_value_pairs) {
  //   memory_addresses[address] = apply_mask(address[value]);
  // }
}

unsigned long part1(const std::vector<std::string> &program) {

  map memory_addresses;

  // For each module, we apply the mask for the given addresses, updating
  // their values and finally we just reduce the values over the hashmap.
  for (auto &module : program) {
    parse_module(module);
    break;
    // update_address(module, memory_addresses);
  }

  return 0UL;
  // return std::accumulate(
  //     memory_addresses.begin(), memory_addresses.end(), 0ULL,
  //     [](long value,
  //        auto &p) { // p is of type std::unordered_map<long,
  //        long>::value_type
  //       return value + p.second;
  //     });
}

int main() {
  // We'll divide the program into subsections, delimited by the masks.
  std::vector<std::string> program =
      parse(std::ifstream{"../../input.txt", std::ios::in});

  // fmt::print("{}\n", program[0]);
  part1(program);

  return 0;
}
