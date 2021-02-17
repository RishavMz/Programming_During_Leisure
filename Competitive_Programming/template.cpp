#include<bits/stdc++.h>
using namespace std;

/*

Custom template based on python style implementation(for less typing and getting task done while maintaining beauty of the code , simply because I love the flexiblity of python typecasting, but tried to do something to fix the frequest frustrating TLE problems )

vector<long> sieveOfEratosthenes(int n);                      Prints prime numbers upto n      

vector<long> splitToLong(string s);                         Splits a string into long values

long stringToLong(string s);                                Converts a string to long

vector<T> distinct(vector<T> v);                            Returns a vector containing distinct elements from a vector(Template based)

vector<T> setToVector(set<T> s);                            Converts a set to a vector(Template based)

vector<string> splitString(const string &s, char delim);     Splits a string to strings based on a delimiter


*/

template <typename T>
set<T> vectorToSet(vector<T> v)
{
    set<T> s;
    for (long i = 0; i < v.size(); i++)
    {
        s.insert(v[i]);
    }
    return s;
}
template <typename T>
vector<T> setToVector(set<T> s)
{
    vector<T> v;
    copy(s.begin(),s.end(),back_inserter(v));
    return v;
}
template <typename T>
vector<T> distinct(vector<T> v)
{
    return setToVector(vectorToSet(v));
}
long stringToLong(string s)
{
    long val;
    int j = 0;
    for(int i = s.size() -1 ;i>=0;i--)
    {
        val += pow(10,j++) * int(s[i]-48);
    }
    return val;
}
vector<long> splitToLong(string s)
{
    vector<long> v;
    string st;
    for(int i=0;i<s.length()+1;i++)
    {
        if(s[i]==' ' || s[i]=='\0')
        {
            v.push_back(stringToLong(st));
            st = "";
        }
        else
        {
            st.push_back(s[i]);
        }
        
    }
    return v;
}
vector<long> sieveOfEratosthenes(int n)
{
	vector<long> sieve;
	vector<long> primes;
	for (int i = 1; i < n + 1; ++i)
    {
	    sieve.push_back(i);   
    }
    sieve[0]=0;
	for (int i = 2; i < n + 1; ++i) 
    {   
		if (sieve[i-1] != 0) 
        {
			primes.push_back(sieve[i-1]);
			for (int j = 2 * sieve[i-1]; j < n + 1; j += sieve[i-1]) 
            {
				sieve[j-1] = 0;
			}
		}
	}
	return primes;
}
vector<string> splitString(const string &s, char delim) 
{ 
    vector<string> elems; 
    stringstream ss(s); 
    string item; 
    while (getline(ss, item, delim)) 
        elems.push_back(item); 
  
    return elems; 
} 


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	cout.tie(NULL);
	#ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
	#endif



















    return 0;
}