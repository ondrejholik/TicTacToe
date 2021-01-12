#include <iostream>
#include <array>
#include <cmath>
#include <cassert>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;


class Board {
  private:
    int board[3][3];
    bool status;
    int p;
    int a;
    set<int> winning_positions = {7, 73, 273, 146, 84, 292, 56, 448};

  public:
    Board(int player, int ai){
      p = player;
      a = ai;
      if((player & ai) != 0){
        status = false;
      }
      else {
        int counter = 0;
        for(int i = 0; i < 3; ++i){
          for(int j = 0; j < 3; ++j){

            if((player & int(pow(2,counter))) != 0){
              board[i][j] = 1;
            }
            else if((ai & int(pow(2,counter))) != 0){
              board[i][j] = 2;
            }
            else {
              board[i][j] = 0;
            }
            ++counter;
          }
        }
      }
    }

    constexpr int isEmpty(int pos){
        int power = int(pow(2,pos));
        return ((power & p) == 0 && (power & a) == 0);
    }

    constexpr int isFull(){
      return (p + a) == 511;
    }

    int whoWins(){
      if(winning_positions.contains(p)){
        return -10;
      }
      
      else if (winning_positions.contains(a)){
        return 10;
      }

      return 0;
    }

    constexpr int findBestMove(int maximizingAI, bool depth){
      if(isFull() || whoWins() != 0){
        return whoWins();
      }

      else if(maximizingAI){
        int value = INT_MIN;
        
         for(int i = 0; i < 9; ++i){
          if(isEmpty(i)){
            int tmp = int(pow(2,i));
            a += tmp;
            value = max(value, findBestMove(false, false));
            a -= tmp;
          }
        }
        if(depth){
          cout << log2(value) << '\n';;
        }
        return value;
      }

      else {
        int value = INT_MAX;

        for(int i = 0; i < 9; ++i){
          if(isEmpty(i)){
            int tmp = int(pow(2,i));
            p += tmp;
            value = min(value, findBestMove(true, false));
            p -= tmp;
          }
        }

        return value;
      }


    }

    int sum(){
      int tmp = 0;
      for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
          tmp += board[i][j];
        }
      }
      return tmp;
    }

    void printBoard(){
      for(int i = 0; i < 3; ++i){
        for(int j = 0; j < 3; ++j){
          cout << board[i][j] << ' ';
        }
        cout << '\n';
      }
    }
};



int main(){


  // load information from two number (a,b) >= 0 && (a,b) <= 2**9
  Board board(0,0);
  board.printBoard();
  cout << board.findBestMove(true, true);

  return 1;

}
