#include <iostream>
#include <fstream>
#include <cctype>
#include <cstdlib>
#include <unordered_map>

std::unordered_map<std::string, int> stringsToNums {
    {"one", 1},
    {"two", 2},
    {"three", 3},
    {"four", 4},
    {"five", 5},
    {"six", 6},
    {"seven", 7},
    {"eight", 8},
    {"nine", 9}
};

int findCalibrationValue(std::string& line) {
        int num1 = -1, num2 = -1;

        for (int i=0; i < line.length(); i++) {
            if (isdigit(line[i])) {
                num1 = line[i] - '0';
                break;
            }
            else {
                for (int subLen=5; subLen >= 3; subLen--) {
                    auto sub = line.substr(i, subLen);
                    auto it = stringsToNums.find(sub);
                    if (it != stringsToNums.end()) {
                        num1 = it->second;
                        break;
                    }
                }

                if (num1 != -1) {
                    break;
                }
            }
        }

        for (int i=line.length()-1; i >= 0; i--) {
            if (isdigit(line[i])) {
                num2 = line[i] - '0';
                break;
            }
            else {
                for (int subLen=5; subLen >= 3; subLen--) {
                    if (i-subLen+1 < 0) {
                        continue;
                    }
                    auto sub = line.substr(i-subLen+1, subLen);
                    auto it = stringsToNums.find(sub);
                    if (it != stringsToNums.end()) {
                        num2 = it->second;
                        break;
                    }
                }

                if (num2 != -1) {
                    break;
                }
            }
        }

        if (num1 == -1 || num2 == -1) {
            std::cout << "Something went wrong: num1=" << num1 << " num2=" << num2 << std::endl;
        }

        return num1*10 + num2;
}

int main(int argc, char* argv[]) {
    std::fstream file("data/input_1_trebuchet.txt", std::ios::in);

    std::string line;
    int left, right;
    int sum = 0;
    while (std::getline(file, line)) {
        sum += findCalibrationValue(line);
    }
    std::cout << sum << std::endl;

    return 0;
}