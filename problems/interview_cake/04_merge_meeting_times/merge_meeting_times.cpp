#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

// [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] -> [(0, 1), (3, 8), (9, 12)]
// [(0, 1), (3, 8), (9, 12)]
 struct Interval {
    int begin;
    int end;
    // Constructors for struct
    Interval(){}
    Interval(int b, int e) {// : begin(b), end(e) {
        begin = b;
        end = e;
    }
};

// Print out the given vector of intervals
void printVector(vector<Interval> x) {
    vector<Interval>::iterator it;
    for (it = x.begin(); it != x.end(); ++it)
        printf("%d,%d\n", it->begin, it->end);
}

bool compare_interval(Interval a, Interval b)
{
    return (a.begin < b.begin);
}
vector<Interval> merge_interval(vector<Interval> arr) {
    if (arr.size() == 0)
        return arr;

    sort(arr.begin(), arr.end(), compare_interval);

    stack<Interval> s;

    s.push(arr[0]);

    for (int i = 1; i < arr.size(); i++)
    {
        Interval top = s.top();

        if (top.end < arr[i].begin)
            s.push(arr[i]);
        else {
            top.end = arr[i].end;
            s.pop();
            s.push(top);
        }
    }

    vector<Interval> result;
    int size = (int)s.size();
    for (int j = 0; j < size; j++) {
        result.push_back(s.top());
        s.pop();
    }

    return result;
}

vector<Interval> merge_interval_tony(vector<Interval> arr) {
    if (arr.size() == 0)
        return arr;

    sort(arr.begin(), arr.end(), compare_interval);

    // iterate through this list and then compare as we go with no stack

    vector<Interval> result;
    vector<Interval>::iterator it;
    Interval cur = Interval(arr[0].begin, arr[0].end);

    for (it = arr.begin()+1; it < arr.end(); it++) {
        if (cur.end < it->begin) {
            // add to list and break
            result.push_back(cur);
            cur.begin = it->begin;
            cur.end = it->end;
            continue;
        } else {
           // merge this one
          cur.end = it->end;
        }
    }

    // merge the last one
    result.push_back(cur);
    return result;
}

int main() {
    vector<Interval> v, x;

    v.push_back(Interval(0,1));
    v.push_back(Interval(3,5));
    v.push_back(Interval(4,8));
    v.push_back(Interval(10,12));
    v.push_back(Interval(9,10));

    vector<Interval> res = merge_interval_tony(v);

    printVector(res);

    return 0;
}
