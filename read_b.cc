#import <fstream>
#import <string>
#import <iostream>
using namespace std;

void read(){
  fstream fs("./result.txt",ios::binary);
  string buf;
  fs.read((char*)&buf,buf.size());
  fs.close();
  ofstream ofs("./result.txt",ios::out);
  ofs<<buf;
  ofs.close();

}
int main()
{
  read();
  return 0;
}
  
