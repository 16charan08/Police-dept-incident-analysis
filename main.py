import argparse
import sqlite3
#import Project0.p0 as project0
import p0



#url = 'http://normanpd.normanok.gov/filebrowser_download/657/2020-02-20%20Daily%20Incident%20Summary.pdf'
def main(url):
    # Download data
    #print(url)

    p0.fetchincidents(url)

    # Extract Data
    incidents = p0.extractincidents()
    #print(len(incidents))

    # Create Dataase
    db = p0.createdb()

    # Insert Data
    p0.populatedb(db, incidents)

    # Print Status
    p0.status(db)


if __name__ == '__main__':
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="The arrest summary url.")
    print("Hello")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
    '''

    main('http://normanpd.normanok.gov/filebrowser_download/657/2020-02-20%20Daily%20Incident%20Summary.pdf')