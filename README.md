
# hibpython

A simple module for [haveibeenpwnd.com](https://haveibeenpwned.com/) written in python which checks if the password has been compromised or found in a data leak using the API from haveibeenpwnd.com.
Please report any bugs/flaws and suggestions to my [twitter](https://twitter.com/y5hn4v)

# Usage
- Clone the repository or download the zip file and extract the file to your folder with your python program
- 
```python
import hibpython.hibp as hibp
```
-
```python
example_variable = hibp.checkpwn("123456")
```
- This will return the value (True, '37509543') where True means the password is compromised and the value 37509543 is the number of times the password was seen in the [haveibeenpwnd.com](https://haveibeenpwned.com/) database

# Features
Right now the module has only one function since the API requires a paid API key.
```python
checkpwn(password)
```
The user should pass the password as argument while calling this function.
This function will check if the password has been compromised and returns True along with the number of times it was seen on the database.Else it returns False.

I am planning on adding one more function soon :D


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## Feedback

If you have any feedback, please reach out to me at https://twitter.com/y5hn4v



## License

[MIT](https://choosealicense.com/licenses/mit/)

