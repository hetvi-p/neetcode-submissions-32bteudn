class Solution {
public:
    bool isPalindrome(string s) {
        
        int start = 0;
        int end = s.size() - 1;

        while (start < end) {
            if (isalnum(s[start]) && isalnum(s[end]) && tolower(s[start]) != tolower(s[end])) {
                cout << s[start] << start << s[end] << end << endl;
                return 0;
            }
            if (!isalnum(s[start])) {
                //cout << s[start] << start << endl;
                start++;
            }
            else if (!isalnum(s[end])) {
                //cout << s[end] << end << endl;
                end--;
            }
            else {
                start ++;
                end --;
            }
        }

        return 1;

        
    }
};
