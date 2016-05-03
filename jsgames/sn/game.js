<script language="javascript">
            
            var theNumber = Math.floor(Math.random()*100+1);
            var countGuesses = 0;
        
            function checkguess() {
                var guess = document.getElementById('guess');
                var output= document.getElementById('output');
                var myNumber = guess.value;
                
                countGuesses++;
                
                if (myNumber < theNumber) {
                    output.value= "Low! Try a Higher Number.";
                    //alert(" Low! Try a Higher Number.")};
                }
                
                else if (myNumber > theNumber){
                    output.value="High! Try a Smaller Number.";
                    //alert("High! Try a Lower Number.");   
                }
                else if (myNumber == theNumber){
                    output.value="Thats the SECRET NUMBER! You got it in " + countGuesses + " tries! Play again...";
                    alert("The number was " + theNumber + "! You Won After " + countGuesses + " Guesses!");
                    theNumber = Math.floor(Math.random()*100+1);
                    countGuesses = 0;
                }
            }
    
        </script>