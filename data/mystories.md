<!-- good bye stories -->
## Generated Story -277470545592324679
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545592325679
* goodbye
    - utter_goodbye
	- action_restart
    - action_restart

## Generated Story -277470545592327679
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545592328679
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545592329679
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545592323679
* goodbye
    - utter_goodbye
	- action_restart
	
<!-- good bye stories -->


<!-- deny stories -->
## Generated Story -277470145592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470245592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470345592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470445592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470645592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470745592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470845592323679
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470945592323679
* deny
    - utter_no_email_sent
	- action_restart
<!-- deny stories -->


<!-- stories starting with only bare inform with complete information and email -->
## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 2732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "kanpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 3732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "jaipur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 4732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with only bare inform with complete information and email -->

<!-- stories starting with only bare inform with complete information and no email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

<!-- stories starting with only bare inform with complete information and no email -->





<!-- stories starting with location inform with complete information and sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
     - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@asdasd.com"}
    - slot{"email": "anurag@asdasd.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with location inform with complete information and sent email -->


<!-- stories starting with location inform with complete information and no sent email -->
## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart


<!-- stories starting with location inform with complete information and no sent email -->


<!-- stories starting with cuisine inform with complete information and sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* send_email{"email": "zjiom@gasf.co.in"}
    - slot{"email": "zjiom@gasf.co.in"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* inform{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with cuisine inform with complete information and sent email -->

<!-- stories starting with cuisine inform with complete information and no sent email -->

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* inform{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

<!-- stories starting with cuisine inform with complete information and no sent email -->



<!-- stories starting with cuisine and location inform, with complete information and sent email -->
## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Guwahati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Guwahati"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Guwahati"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

<!-- stories starting with cuisine and location inform, with complete information and sent email -->


<!-- stories starting with cuisine and location inform, with complete information and no sent email -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -2126870891193165514
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bhopal"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## Generated Story -2126870891193165654
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart


## Generated Story -2126870891193165634
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart


## Generated Story -2126870891193165610
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Kozhikode"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kozhikode"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Kozhikode"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart


## Generated Story -2126870891193165613
* greet
    - utter_greet
* inform{"cuisine": "thai", "location": "mumbai"}
    - slot{"cuisine": "thai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart
<!-- stories starting with cuisine and location inform, with complete information and no sent email -->

<!-- misc -->
## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326629
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326379
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326379
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326379
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326379
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592326379
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart


<!-- misc -->
<!-- leave in between -->


## Generated Story -277470545592426679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592426679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592426679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## Generated Story -277470545592426679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart


## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545595326679
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545596326679
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545792326679
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470548592326679
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -277470545502322679
* greet
    - utter_greet
* inform{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

<!-- leave in between -->




<!-- condition checkpoints -->

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## Generated Story 1732454364351689134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story 5732454364351689134
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gasf.com"}
    - slot{"email": "uyhbkjn@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -277470545592326678
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gasf.com"}
    - slot{"email": "asdsdad@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- condition checkpoints -->

<!-- all the information in one go -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- all information in one go. -->



<!-- starting with budget and location -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- starting with cuisine and budget -->

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## Generated Story -2126870891193165614
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

