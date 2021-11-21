char solution(string s) {
    unordered_map<char, int> arr;
    
    for (char i = 'a'; i <= 'z'; ++i)
        arr[i] = 0;
    
    for (char ch : s)
        arr[ch] += 1;
        
    for (char ch : s)
        if (arr[ch] == 1)
            return ch;
    return '_';
}
