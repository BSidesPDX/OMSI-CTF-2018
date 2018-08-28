#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <regex.h>

#define LEN 25

int serialCheck(char *serial)
{
    /*
       BSidesPDX{****_****_****}
     * starts at 11th char
     * 11-14
     * 16-19
     * 21-24
     */

    int pos = 11-1;

    if (strncmp(serial + pos, "1337", 4) == 0)
    {
        pos += 5;
        if (strncmp(serial + pos, "dead", 4) == 0)
        {
            pos += 5;
            if (strncmp(serial + pos, "beef", 4) == 0)
            {
                return 1;
            }
            else
                return 0;
        }
        else
            return 0;

	}
	else
		return 0;
}


// https://stackoverflow.com/questions/1631450/c-regular-expression-howto/1631458
bool reg_matches(const char *str, const char *pattern)
{
    regex_t re;
    int ret;

    if (regcomp(&re, pattern, REG_EXTENDED) != 0)
        return false;

    ret = regexec(&re, str, (size_t) 0, NULL, 0);
    regfree(&re);

    if (ret == 0)
        return true;

    return false;
}

bool format(char *serial)
{
    static const char *pattern = "BSidesPDX\\{.*{4}_.*{4}_.*{4}}";

    if (reg_matches(serial, pattern))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main(int argc, char *argv[])
{
    char serial[LEN];

    printf("Please enter serial\n");

    fgets(serial, LEN+1, stdin);

    if (format(serial))
    {
		if (serialCheck(serial))
		{
			printf("Serial is correct\n");
		}
		else
			printf("Incorrect serial\n");
	}
    else
    {
        printf("The serial must be in the format of BSidesPDX{XXXX_XXXX_XXXX}\n");
    }

}
