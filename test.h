#ifndef __TEST_H__

#define __TEST_H__

#ifndef __SUBS__
#include <stdio.h>
#define PRINT(fmt, ...)	printf(fmt);
#else
#define PRINT(...)
#endif

void test(void);

#endif /* end of include guard: __TEST_H__ */
