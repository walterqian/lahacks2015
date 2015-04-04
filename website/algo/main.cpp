#include <list>
#include <string>
#include <vector>

using namespace std;

struct User {
	User (string source, string destination, vector<string> times);
	string src;
	string dest;
	bool matched;
	string depart_station;
	double savings;
	string lines;
	vector<string> time;
};

struct Places {
	Places(string id, vector<string> times);
	string name;
	vector<string> times;
};

User::User(string source, string destination, vector<string> times): src(source), dest(destination), time(times),
		matched(false), depart_station(""), savings(0), lines(""){
}

Places::Places(string id, vector<string> times): name(id), times(times) {
}

int main () {

}
