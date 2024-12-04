#include <algorithm>
#include <cstddef>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <ostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <vector>

template <typename T> void print(const T &value) {
  std::cout << value << std::endl;
}

template <typename T, size_t N> constexpr size_t arr_len(const T (&arr)[N]) {
  return N;
}

template <typename T, size_t N> void sort_numeric_array(T (&arr)[N]) {
  static_assert(std::is_arithmetic<T>::value,
                "Array type must be a numeric type");
  std::sort(std::begin(arr), std::end(arr));
}

template <typename T, size_t N> bool is_positive(T (&arr)[N]) {
  static_assert(std::is_arithmetic<T>::value, "Array must be numeric type");
  for (auto value : arr) {
    if (value <= 0)
      return false;
  }
  return true;
}

bool all_distances_in_range(int arr[], size_t size, int low, int high) {
  for (size_t i = 0; i < size; ++i) {
    if (abs(arr[i]) < low || abs(arr[i]) > high) {
      return false;
    }
  }

  return false;
}

bool all_distances_in_range(const std::vector<int> &vec, int low, int high) {
  for (const auto &val : vec) {
    int abs_val = std::abs(val);
    if (abs_val < low || abs_val > high) {
      return false;
    }
  }
  return true;
}

template <typename T, size_t N> bool is_negative(T (&arr)[N]) {
  static_assert(std::is_arithmetic<T>::value, "Array must be numeric type");
  for (auto value : arr) {
    if (value >= 0)
      return false;
  }
  return true;
}

template <typename T> bool is_negative(const std::vector<T> &vec) {
  static_assert(std::is_arithmetic<T>::value,
                "Vector elements must be numeric types");
  for (const auto &value : vec) {
    if (value >= 0) {
      return false;
    }
  }
  return true;
}

template <typename T> bool is_positive(const std::vector<T> &vec) {
  static_assert(std::is_arithmetic<T>::value,
                "Vector elements must be numeric types");
  for (const auto &value : vec) {
    if (value <= 0) {
      return false;
    }
  }
  return true;
}

template <size_t N> bool is_safe(const int (&arr)[N]) {
  int len = arr_len(arr);
  int diffs[N - 1];

  for (int i = 1; i < len; ++i) {
    diffs[i - 1] = arr[i] - arr[i - 1];
    std::cout << diffs[i - 1] << std::endl;
  }

  if (!(is_positive(arr) && is_negative(arr))) {
    return true;
  }

  return false;
}

bool is_vector_safe(const std::vector<int> &vec) {
  if (vec.size() < 2) {
    return false;
  }

  std::vector<int> diffs;
  for (size_t i = 1; i < vec.size(); ++i) {
    int diff = vec[i] - vec[i - 1];
    diffs.push_back(diff);
  }

  bool is_increasing =
      std::all_of(diffs.begin(), diffs.end(), [](int d) { return d > 0; });
  bool is_decreasing =
      std::all_of(diffs.begin(), diffs.end(), [](int d) { return d < 0; });

  if (!(is_increasing || is_decreasing)) {
    return false;
  }

  bool diffs_in_range = all_distances_in_range(diffs, 1, 3);

  return diffs_in_range;
}

std::vector<std::string> split_string(const std::string &str,
                                      const std::string &delimiter) {
  std::vector<std::string> tokens;
  size_t prev = 0, pos = 0;

  while ((pos = str.find(delimiter, prev)) != std::string::npos) {
    if (pos > prev) {
      tokens.push_back(str.substr(prev, pos - prev));
    }
    prev = pos + delimiter.length();
  }

  if (prev < str.length()) {
    tokens.push_back(str.substr(prev));
  }

  return tokens;
}

std::vector<int> create_int_vector(const std::vector<std::string> &str_vector) {
  std::vector<int> int_vector;

  for (const auto &str : str_vector) {
    int_vector.push_back(std::stoi(str));
  }

  return int_vector;
}

std::string read_file(std::string filepath) {
  std::ifstream InputFile(filepath);

  if (!InputFile.is_open()) {
    throw std::runtime_error("failed to load the file: " + filepath);
  }
  std::stringstream buffer;
  buffer << InputFile.rdbuf();

  InputFile.close();

  return buffer.str();
}

int part1(std::string &input_filepath) {
  std::string content = read_file(input_filepath);
  int safe = 0;
  std::vector<std::string> reports = split_string(content, "\n");

  for (auto report : reports) {
    std::vector<std::string> report_levels_str = split_string(report, " ");
    std::vector<int> report_levels = create_int_vector(report_levels_str);
    if (is_vector_safe(report_levels)) {
      safe++;
    }
  }

  return safe;
}

int main() {
  std::string filepath = "./input.txt";

  print(part1(filepath));
  return 0;
}
