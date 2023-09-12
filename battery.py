def count_batteries_by_health(present_capacities):
  # Initializing the count variables
  healthy_count = 0
  exchange_count = 0
  failed_count = 0
    
  # Rated capacity of the battery
  rated_cap = 120
  
  # Lists created to classify the present capacitites, whether the battery is healthy, exchanged or failed.
  healthy_batteries =[]
  exchange_batteries=[]
  failed_batteries=[]
  status_count={}
  
  #Calculating the SoH for each battery by looping through the present capacities given
  for cap in present_capacities:
      
      #Formula for calculating SoH for each present capacity
      SoH = 100 * cap / rated_cap
      
      # Classifying the batteries based on SoH values obtained
      if SoH > 80:
          healthy_count += 1
          healthy_batteries.append(cap)
      elif 63 <= SoH <= 80:
          exchange_count += 1
          exchange_batteries.append(cap)
      else:
          failed_count += 1
          failed_batteries.append(cap)
          
  status_count= {
      "healthy": healthy_count,
      "exchange": exchange_count,
      "failed": failed_count,
    }
  return status_count, healthy_batteries, exchange_batteries, failed_batteries


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts, h, e, f = count_batteries_by_health(present_capacities)
  print("The number of batteries that are healthy, exchange and failed are:")
  print(counts)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  for i in h:
      print("The batteries with present capacity",i, "are healthy")
  for i in e:
      print("The batteries with present capacity",i, "are to be exchanged")
  for i in f:
      print("The batteries with present capacity",i, "are failed")
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
