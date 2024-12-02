#include <cstdlib>
#include <fstream>
#include <iostream>
#include <ostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

/*std::tuple<std::string, std::string> split_string(text std::string) {*/
/*	return*/
/*}*/

int stringLen(std::string &text) {
  int length = 0;
  for (size_t i = 0; i < text.size(); ++i) {
    length++;
  }
  return length;
}

template <typename T> void print(const T &value) {
  std::cout << value << std::endl;
}

// make a function that returns array of strings
/*std::string* */

int count_sequence_occurences(std::string &text, std::string sequence) {
  int text_len = stringLen(text);
  int seq_len = stringLen(sequence);
  int xdd = 0;
  print(seq_len);
  print(text_len);

  for (int i = 0; i <= text_len - seq_len; i++) {
    std::string curr_substr = text.substr(i, seq_len);
    print(text.substr(i, i + seq_len));
    std::cout << i << "  " << seq_len << "  " << seq_len + i << std::endl;
    if (curr_substr == sequence) {
      xdd += 1;
    }
  }
  return xdd;
}

/*std::string *split_string(std::string separator) {}*/

std::string read_file(const std::string &file_path) {
  std::ifstream InputFile(file_path);
  if (!InputFile.is_open()) {
    throw std::runtime_error("Failed to open the file: " + file_path);
  }
  std::stringstream buffer;
  buffer << InputFile.rdbuf();
  InputFile.close();
  return buffer.str();
}

int count_lines(std::string &text) {
  int line_count = 0;
  for (char c : text) {
    if (c == '\n') {
      line_count++;
    }
  }
  if (!text.empty() && text.back() != '\n') {
    line_count++;
  }

  return line_count;
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

void bubble_sort(std::vector<int> &arr) {
  int len = arr.size();
  for (int i = 0; i < len - 1; ++i) {
    for (int j = 0; j < len - i - 1; ++j) {
      if (arr[j] > arr[j + 1]) {
        std::swap(arr[j], arr[j + 1]); // Use std::swap for swapping
      }
    }
  }
}

void create_arrays(const std::vector<std::string> &lines,
                   std::vector<int> &arrLeft, std::vector<int> &arrRight) {
  for (const auto &line : lines) {
    if (line.empty()) {
      continue;
    }

    std::vector<std::string> numbers = split_string(line, " ");

    if (numbers.size() != 2) {
      std::cerr << "Invalid line format: " << line << std::endl;
      continue;
    }

    try {
      arrLeft.push_back(std::stoi(numbers[0]));
      arrRight.push_back(std::stoi(numbers[1]));
    } catch (const std::invalid_argument &e) {
      std::cerr << "Invalid number in line: " << line << std::endl;
      continue;
    }
  }
}

int part1(std::vector<int> left, std::vector<int> right) {
  int len = left.size();
  int result = 0;
  for (int i = 0; i < len; ++i) {
    result += abs(left[i] - right[i]);
  }
  return result;
}

int count_occurences(std::vector<int> &vec, int item) {

  int count = 0;
  for (int i = 0; i < vec.size(); ++i) {
    if (vec[i] == item) {
      count++;
    }
  }
  return count;
}

int part2(std::vector<int> left, std::vector<int> right) {
  int result = 0;

  for (int i = 0; i < left.size(); ++i) {
    result += left[i] * count_occurences(right, left[i]);
  }

  return result;
}

int main() {
  std::string file_content;
  try {
    file_content = read_file("./input.txt");
  } catch (const std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
    return 1;
  }

  std::vector<std::string> lines = split_string(file_content, "\n");

  lines.erase(std::remove(lines.begin(), lines.end(), ""), lines.end());

  std::vector<int> arrLeft;
  std::vector<int> arrRight;

  create_arrays(lines, arrLeft, arrRight);
  bubble_sort(arrLeft);
  bubble_sort(arrRight);

  for (size_t j = 0; j < arrLeft.size(); ++j) {
    std::cout << "left[" << j << "]: " << arrLeft[j] << std::endl;
  }

  for (size_t j = 0; j < arrRight.size(); ++j) {
    std::cout << "right[" << j << "]: " << arrRight[j] << std::endl;
  }

  int result = part1(arrLeft, arrRight);
  std::cout << "Results: " << result << std::endl;

  int result2 = part2(arrLeft, arrRight);
  std::cout << "Results: " << result2 << std::endl;

  return 0;
}
