#pragma once

#include <iostream>

// simplistic printing utility function for containers
// generalize to any container that supports ForwardIterator?
template <typename T>
void print_container(const std::vector<T> &cont, const size_t &N) {
  std::for_each_n(std::begin(cont), N - 1,
                  [](const T &elem) { std::cout << elem << ", "; });
  std::cout << *(std::next(std::begin(cont), N - 1));
  std::cout << "\n";
}