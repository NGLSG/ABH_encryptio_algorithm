#import <fstream>
#include <string>
using namespace std;

void write(){
  ifstream ifs("./temp.txt",ios::in);
  string buf;
  while(getline(ifs,buf)){}
  ifs.close();
  fstream fs("./temp.txt",ios::binary);
  fs.write((const char*)&buf,buf.size());
  fs.close();

}
int main()
{
  write();
  return 0;
}
