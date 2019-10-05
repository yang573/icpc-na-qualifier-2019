
#include <stdio.h>
#include <vector>

using namespace std;

int main() {

    int numNumbers;
    scanf("%d", &numNumbers);


    double runningAvgForward = 0;
    double maxAvgForward = 0;
    double runningSumForward = 0;
    int maxAvgIndex = -1;

    double runningAvgBackward = 0;
    double maxAvgBackward = 0;
    double runningSumBackward = 0;
    int maxAvgIndexB = -1;

    vector<int> nums;

    for (int i = 0; i < numNumbers; i++) {
        int temp;
        scanf("%d", &temp);
        nums.push_back(temp);
    }

    for (int i = 0; i < nums.size(); i++) {
        runningSumForward += nums[i];
        runningAvgForward = runningSumForward / (i+1);
        if (runningAvgForward > maxAvgForward) {
            maxAvgForward = runningAvgForward;
            maxAvgIndex = i;
        }
    }

    for (int i = nums.size() - 1; i >= 0; i--) {
        runningSumBackward += nums[i];
        runningAvgBackward = runningSumBackward / (nums.size() - i);
        if (maxAvgBackward > runningAvgBackward) {
            maxAvgBackward = runningAvgBackward;
            maxAvgIndexB = i;
        }
    }



    double finalAverage = 0;
    // printf("maxAvgIndex: %d", maxAvgIndex);
    // int numA = maxAvgIndex + 1;
    // maxAvgForward *= numA;

// printf("maxAvgForward: %d", maxAvgForward);

    if (maxAvgForward >= maxAvgBackward) {
        
        finalAverage = maxAvgForward;
    }
    else if (maxAvgBackward > maxAvgForward) {
        finalAverage = maxAvgBackward;
    }
    else {
        finalAverage = 0;
    }

    // if (maxAvgBackward > maxAvgForward) {
    //     int numB = nums.size() - maxAvgIndexB;
    //     maxAvgBackward *= numB;
    //     finalAverage = maxAvgForward + maxAvgBackward;
    //     finalAverage /= (numA + numB);
    // }
    // else {
    //     finalAverage = maxAvgForward / numA;
    // }

    printf("%lf\n", finalAverage);

    return 0;
}
