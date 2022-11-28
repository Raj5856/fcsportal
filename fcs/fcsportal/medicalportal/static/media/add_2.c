#include <stdio.h>
#include <inttypes.h>

int64_t add(int64_t, int64_t, int64_t, int64_t);


int main() {
	int x,y,w,z;
//	printf("Enter First Number \n");
	scanf("%d",&x);
//	printf("Enter Second Number\n");
	scanf("%d",&y);
	scanf("%d",&w);
	scanf("%d",&z);
    printf("%ld\n", add(x, y,w,z));
    return 0;
}
