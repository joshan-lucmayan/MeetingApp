require 'sqlite3'

begin
  # Connect to the SQLite database created by Python
  db = SQLite3::Database.open "meetings.db"
  
  puts "--- Meeting Schedule Report ---"
  puts "%-20s | %-20s" % ["Host", "Date/Time"]
  puts "------------------------------------------"
  
  # Select meeting details from your table
  db.execute("SELECT host, date_time FROM meeting") do |row|
    puts "%-20s | %-20s" % [row[0], row[1]]
  end
rescue SQLite3::Exception => e
  puts "Exception occurred: #{e}"
ensure
  db.close if db
end