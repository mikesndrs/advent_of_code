#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

#include "01.H"

typedef long long ll;

ll get_top_n(int n){
  std::ifstream file("../inputs/01.txt");
  std::string line;
  
  std::vector<ll> top_list(n, 0);
  ll result;
  ll curr_elf = 0;

  while(std::getline(file, line)) {
    if(line != ""){
      curr_elf += std::stoll(line);
    }
    else{
      if(curr_elf > top_list.front()){
        top_list.front() = curr_elf;
        std::sort(top_list.begin(), top_list.end());
      }
      curr_elf = 0;
    }
  }

  result = accumulate(top_list.begin(), top_list.end(), 0);

  return result;
}

int main(){
  // puzzle 1
  int input1 = 1;  
  std::cout << get_top_n(input1) << "\n";
  // puzzle 2
  int input2 = 3;  
  std::cout << get_top_n(input2) << "\n";
  return 0;
}
