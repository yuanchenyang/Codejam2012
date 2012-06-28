#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXL 1001

int reqStar[MAXL][2];
bool done[MAXL][2];

int main ()
{
	int T, N, i, stars, prevs, moves, diff;
	scanf("%d",&T);
	
	for ( int cnt = 1; cnt <= T; cnt++ )
	{
		scanf("%d",&N);
		stars = 0;
		prevs = -1;
		moves = 0;
		for ( i = 1; i <= N; i++ ) done[i][0] = done[i][1] = false;
		for ( i = 1; i <= N; i++ ) scanf("%d %d",&reqStar[i][0],&reqStar[i][1]);
		
		while ( stars > prevs ) 
		{
			//Find all 2 star levels you can currently complete
			
			while ( stars > prevs )
			{
				prevs = stars;
				
				for ( i = 1; i <= N; i++ )
				{
					if ( done[i][1] ) continue;
					
					if ( stars >= reqStar[i][1] )
					{
						if ( done[i][0] ) stars += 1;
						else stars += 2;
						done[i][0] = true;
						done[i][1] = true;
						moves++;
					}
				}
			}
		
			//Take the 1 star level where 2 star level is farthest
			
			diff = 0;
			
			for ( i = 1; i <= N; i++ )
			{
				if ( done[i][0] ) continue;
				if ( stars < reqStar[i][0] ) continue;
				else diff = max(diff,reqStar[i][1]-reqStar[i][0]);
			}
			
			for ( i = 1; i <= N; i++ )
			{
				if ( done[i][0] ) continue;
				if ( stars < reqStar[i][0] ) continue;
				if ( reqStar[i][1]-reqStar[i][0] == diff )
				{
					done[i][0] = true;
					stars += 1;
					moves++;
					break;
				}
			}
		}
		
		if ( stars < 2 * N ) printf("Case #%d: Too Bad\n",cnt);
		else printf("Case #%d: %d\n",cnt,moves);
	}
}