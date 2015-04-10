using System;

namespace Bob
{

    public class Bob
    {
        public bool Hey(string phrase)
        {   
            if (IsSilence(phrase)){
                return "Fine. Be that way!";
            }
            if (IsQuestion(phrase)){
                return "Sure.";
            }
            if (IsYell(phrase)){
                return "Whoa, chill out!";
            }
            else{
                return "Whatever.";
            }
        }
        private bool IsSilence(string phrase)
        {
            return phrase.Trim() = "";
        }
        private bool IsQuestion(string phrase)
        {
            return phrase.Trim().EndsWith("?");
        }
        private bool IsYell(string phrase)
        {
            return phrase.ToUpper() == phrase;
        }
    }
}
