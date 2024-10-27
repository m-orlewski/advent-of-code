#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cctype>

bool isPartAround(const std::vector<std::vector<char>>& schematic, const int i, const int j) {
    for (int x=std::max(0, i-1); x <= std::min((int)schematic[i].size()-1, i+1); x++) {
        for (int y=std::max(0, j-1); y <= std::min((int)schematic.size()-1, j+1); y++) {
            if (schematic[x][y] != '.' && !isdigit(schematic[x][y])) return true;
        }
    }

    return false;
}

int sumAllPartNumbers(const std::vector<std::vector<char>>& schematic) {
    int sum = 0;
    for (int i=0; i < schematic.size(); i++) {
        for (int j=0; j < schematic[i].size(); j++) {
            if (!isdigit(schematic[i][j])) continue;

            // found first digit, scan around it and continue to next digit
            int digit = 0;
            bool partFound = false;
            do {
                digit = digit*10 + (schematic[i][j] - '0'); // extend currently processed digit
                if (!partFound) partFound = isPartAround(schematic, i, j); // check if part was found
            } while (++j < schematic[i].size() && isdigit(schematic[i][j])); // scan until digit ends

            if (partFound) sum += digit;
        }
    }

    return sum;
}

int getFullPartNumber(const std::vector<std::vector<char>>& schematic, int i, int j) {
    while (j > 0 && isdigit(schematic[i][j-1])) j--; // go left to the first digit

    int digit = 0;
    while (j < schematic.size() && isdigit(schematic[i][j])) {
        digit = digit*10 + (schematic[i][j] - '0');
        j++;
    }

    return digit;
}

int getGearRatio(const std::vector<std::vector<char>>& schematic, const int i, const int j) {
    // 1) check on the sides i,j-1 and i,j+1
    // 2) check above i-1, j
    // 3) if there is a part above, skip checking i-1,j-1 and i-1, j+1 else check both
    // 4) check below i+1, j
    // 5) if there is a part below, skip checking i+1, j-1 and i+1, j+1 else check both

    int foundParts = 0;
    int gearRatio = 1;
    
    bool skipLeft = (j == 0);
    bool skipRight = (j == schematic[i].size());
    if (!skipLeft && isdigit(schematic[i][j-1])) {
        gearRatio *= getFullPartNumber(schematic, i, j-1);
        foundParts++;
    }
    if (!skipRight && isdigit(schematic[i][j+1])) {
        gearRatio *= getFullPartNumber(schematic, i, j+1);
        foundParts++;
    }

    if (i != 0) {
        if (isdigit(schematic[i-1][j])) {
            gearRatio *= getFullPartNumber(schematic, i-1, j);
            foundParts++;
        }
        else {
            if (!skipLeft && isdigit(schematic[i-1][j-1])) {
                gearRatio *= getFullPartNumber(schematic, i-1, j-1); 
                foundParts++;
            }
            if (!skipRight && isdigit(schematic[i-1][j+1])) {
                gearRatio *= getFullPartNumber(schematic, i-1, j+1);
                foundParts++;
            }
        }
    }

    if (i != schematic.size()) {
        if (isdigit(schematic[i+1][j])) {
            gearRatio *= getFullPartNumber(schematic, i+1, j);
            foundParts++;
        }
        else {
            if (!skipLeft && isdigit(schematic[i+1][j-1])) {
                gearRatio *= getFullPartNumber(schematic, i+1, j-1);
                foundParts++;
            }
            if (!skipRight && isdigit(schematic[i+1][j+1])) {
                gearRatio *= getFullPartNumber(schematic, i+1, j+1);
                foundParts++;
            }
        }
    }

    return (foundParts == 2) ? gearRatio : 0;
}

int sumAllGearRatios(const std::vector<std::vector<char>>& schematic) {
    int sum = 0;

     for (int i=0; i < schematic.size(); i++) {
        for (int j=0; j < schematic[i].size(); j++) {
            if (schematic[i][j] != '*') continue;

            sum += getGearRatio(schematic, i, j);
        }
     }

    return sum;
}

int main(int argc, char* argv[]) {
    std::vector<std::vector<char>> schematic;
    std::fstream file("data/input_3_gear_ratios.txt", std::ios::in);

    std::string line;
    while (std::getline(file, line)) {
        schematic.push_back(std::vector<char>(line.begin(), line.end()));
    }

    std::cout << sumAllPartNumbers(schematic) << std::endl;
    std::cout << sumAllGearRatios(schematic) << std::endl;

    return 0;
} 