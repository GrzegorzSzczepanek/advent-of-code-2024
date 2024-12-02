#include <fstream>
#include <iostream>
#include <iterator>
#include <ostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>
/*#include <tuple>*/

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

void bubble_sort(int arr[], int len) {
  for (int i = 0; i < len; ++i) {
    for (int j = i + 1; j < len; ++j) {
      if (arr[i] > arr[j]) {
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
      }
    }
  }
}

/*int std::vector<std::string> */

void create_arrays(const std::vector<std::string> &lines,
                   std::vector<int> &arrLeft, std::vector<int> &arrRight) {
  for (const auto &line : lines) {
    if (line.empty()) {
      continue;
    }

    std::vector<std::string> numbers =
        split_string(line, " "); // Split on any whitespace

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

  // Print the arrays
  for (size_t j = 0; j < arrLeft.size(); ++j) {
    std::cout << "left[" << j << "]: " << arrLeft[j] << std::endl;
  }

  for (size_t j = 0; j < arrRight.size(); ++j) {
    std::cout << "right[" << j << "]: " << arrRight[j] << std::endl;
  }
}

int main() {
  std::string file_content;
  try {
    file_content = read_file("./input.txt");
  } catch (const std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
    return 1;
  }

  // Split the file content into lines
  std::vector<std::string> lines = split_string(file_content, "\n");

  // Remove any empty strings
  lines.erase(std::remove(lines.begin(), lines.end(), ""), lines.end());

  // Create vectors for left and right arrays
  std::vector<int> arrLeft;
  std::vector<int> arrRight;

  create_arrays(lines, arrLeft, arrRight);

  return 0;
}
