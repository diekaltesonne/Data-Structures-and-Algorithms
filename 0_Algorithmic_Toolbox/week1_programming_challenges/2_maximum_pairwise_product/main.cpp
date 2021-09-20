#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProduct_fast(const std::vector<int>& numbers){
    size_t n = numbers.size();

    int max_index_1 = -1;
    for(size_t i =0 ;i<n;++i){
        if( (max_index_1 ==-1)|| (numbers[i]>numbers[max_index_1])){
            max_index_1 = i;
        }
    }

    int max_index_2 = -1;
    for(size_t j = 0 ;j<n;++j){
        if((j != max_index_1)&&((max_index_2 ==-1)||(numbers[j]>numbers[max_index_2]))){
            max_index_2 =j;
        }
    }

    return ((long long)numbers[max_index_1])*(numbers[max_index_2]);

}

int main(){
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);

    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct_fast(numbers) << "\n";
    return 0;
}
