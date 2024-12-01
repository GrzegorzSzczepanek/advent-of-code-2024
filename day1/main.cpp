#include <fstream>
#include <iostream>
#include <ostream>
#include <string>
#include <tuple>
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

void read_file(std::string file_path) {
  std::string fileContent;
  std::ifstream InputFile(file_path);

  while (std::getline(InputFile, fileContent)) {
    std::cout << fileContent << std::endl;
  }
  InputFile.close();
}

int main() {
  /*read_file("./input.txt");*/
  std::string text = "hhuuuh";
  std::string sequence = "uu";
  int xd = count_sequence_occurences(text, sequence);

  /*count_sequence_occurences("huj", "uj");*/
  return 0;
}
