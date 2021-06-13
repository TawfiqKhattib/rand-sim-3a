import csv


class CSV_Manager:
    def __init__(self, filename):
        self.filename = filename

    def get_csv_as_dicts(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
            return self.to_dict(rows)

    def to_dict(self, rows):
        keys = rows[0]
        all_data = []

        for row in rows:
            data_dict = {}
            for i in range(0, len(row)):
                data_dict[keys[i]] = row[i]
            all_data.append(data_dict)

        return all_data

    def manag_properties(self):
        all_Mappingdata={};
        all_data = self.get_csv_as_dicts();
        for article in all_data:
            if (len(all_Mappingdata.keys())>0) and (article["author"] in all_Mappingdata.keys()):
                all_Mappingdata[article["author"]].append(article);
            else:
                all_Mappingdata[article["author"]]= [article]
            if (len(all_Mappingdata.keys())>0) and (article["category"] in all_Mappingdata.keys()):
                all_Mappingdata[article["category"]].append(article);
            else:
                all_Mappingdata[article["category"]]= [article]

        return all_Mappingdata;


