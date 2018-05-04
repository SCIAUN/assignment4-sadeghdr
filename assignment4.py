def port_scanner():
    """
    write a port scanner using nmap library
    for scanning 10 arbitrary hosts and and ports between
    21-1000 then write the result to a file using
    write_to_file function
    """
    nm = nmap.PortScanner()
    nm.scan(ports, '21-1000')    
    print(ports)    
    print(nm.all_hosts())  
    for host_names in nm.all_hosts():
         print(ports)       
         ports = nm[host_names].get('tcp') 
         print(ports)       
         write_to_file(ports)
    return ports
    
def write_to_file(contents):
    """
    first remove the pass from function body
    then write your code
    :param contents: the result that should be written to file
    :return: true if the writing successfull and false if can't
    """
    
    f = open('result_of_nmap', 'sadegh4') 
    f.write(str(contents))

    pass


def main():
    hosts = {    
        'p30download.com',  
        'google.com',    
        'downloadha.com', 
        'iaun.ac.ir',   
        'maktabkhooneh.org',  
        'soft98.ir',
    }
      for host_name in hosts:    
        port_scanner(host_name)

main()
