using System;

public class Bob
    {
        public string Hey(string phrase)
        {   
            if (IsSilence(phrase)){
                return "Fine. Be that way!";
            }
	    if (IsYell(phrase)){
                return "Whoa, chill out!";
            }
            if (IsQuestion(phrase)){
                return "Sure.";
            }
            else{
                return "Whatever.";
            }
        }
        private bool IsSilence(string phrase)
        {
            return phrase.Trim() == "";
        }
        private bool IsQuestion(string phrase)
        {
            return phrase.Trim().EndsWith("?");
        }
        private bool IsYell(string phrase)
        {
            return phrase.ToUpper() == phrase && System.Text.RegularExpressions.Regex.IsMatch(phrase, "[a-zA-Z]+");
        }
    }

