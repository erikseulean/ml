

###### TransactionDT:
 - smallest is 86400 - which makes me thinks that the unit here is seconds, given that 86400 stands for a day
 - max values is 15811131 - which is 184 days later (so the data is basically 6 months of card details)

We can compute the transaction day, by dividing by 86400 and take the integer part. This transforms from seconds to days, so we can have a better idea. This makes sure that Transaction and D1-D15 are on the same scale.

Another idea to consider here, is to try to do training on consecutive time intervals. For example, we cannot take random samples for training/validation, because you cannot predict isFraud using day 182 to predict card fraud on day 3, for the same card. (this if we can figure out a way to find out the cards)


- TransactionAmt - just the amout transacted
- card1 - card6 - are basically "user" identification details such as card type, bank details, etc. These could be used to actually
aggregate data, amongst the adresses
- from the forum, if for one client, a transaction is fraudulent, everything is set to fraudulent, so we should de-duplicate the data before actually trying to do something. Here's an example for this:



|Card1| Addr1| Amt| TransactionId| IsFraudulent|
|-----|------|----|--------------| -------------|
|1| 2| 123| 1122| 1|
|1| 2| 341| 2311| 1|
|3| 4| 444| 1231| 0|
|4| 5| 232| 1111| 0|

First two rows are identifying the same credit card, given that it has the same bank details and the same address, hence we could just de-duplicate all the rows. 

To be able to aggregate, we could just use mean on the rest of the values, such as amount, and all the other features.