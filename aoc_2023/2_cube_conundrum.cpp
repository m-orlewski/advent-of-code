#include <iostream>
#include <sstream>
#include <unordered_map>
#include <cctype>
#include <fstream>

std::unordered_map<char, int> bagContents {
    {'r', 12},
    {'g', 13},
    {'b', 14}
};

int processGame(const std::string& line) {
    std::istringstream s(line);
    std::string placeholder, set;
    int gameNumber;

    // read game number
    s >> placeholder >> gameNumber >> placeholder;

    int count;
    std::string color;
    while (std::getline(s, set, ';')) {
        // std::cout << "Processing set: " << set << std::endl;
        std::istringstream ss(set);
        do {
            ss >> count >> color;
            
            if (count > bagContents[color[0]]) return 0;
        } while (color[color.length()-1] == ',');
    }

    // std::cout << "Game is good\n";
    return gameNumber;
}

int main(int argc, char* argv[]) {

    std::fstream file("data/input_2_cube_conundrum.txt", std::ios::in);
    int result = 0;
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
        result += processGame(line);
    }
    std::cout << result << std::endl;

    // auto line  = "Game 2: 3 blue, 1 green, 2 red; 2 red, 2 green, 5 blue; 3 green, 10 blue; 8 red, 1 blue; 3 red, 1 green, 5 blue; 1 blue, 5 red, 3 green";
    // std::cout << processGame(line);

    return 0;
}