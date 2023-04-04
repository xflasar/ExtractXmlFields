import xml.etree.ElementTree as ET

print("Welcome to the XML Extractor!\nMade by: xSupeFly\nVersion: 1.0\nDiscord: xSupeFly#2911\n\nThis program will extract fields from an XML file and write them to a text file.\nThe fields to extract and the output format can be specified by the user.\nThe program will prompt the user for the following information:\n1. The XML structure to extract (e.g. PhysicalItems/PhysicalItem/Id/)\n2. The names of the fields to extract (separated by commas)\n3. The path to the input XML file\n4. The output format string (e.g. '{SubtypeId}.{TypeId}, {Volume}')\n5. The path to the output text file\n\n")


# prompt the user to enter the XML structure to extract
xml_structure = input("Enter the XML structure to extract ( if fields are located in PhysicalItem then stop at PhysicalItem and in fields input use /Id/FieldToExtract) (e.g. PhysicalItems/PhysicalItem/Id/): ")

# prompt the user to enter the names of the fields to extract
fields = input("Enter the names of the fields to extract (separated by commas): ").split(",")

# prompt the user to enter the path to the input XML file
input_file = input("Enter the path to the input XML file: ")

# prompt the user to enter the output format string
output_format = input("Enter the output format string (e.g. '{SubtypeId}.{TypeId}, {Volume}'): ")

# prompt the user to enter the path to the output text file
output_file = input("Enter the path to the output text file: ")

# create a new file to write the extracted fields to
with open(output_file, "w") as file:

    # parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # iterate over the elements matching the user-specified structure
    for element in root.findall(xml_structure):

        # extract the user-specified fields from the element
        values = {}
        for field in fields:
            field_element = element.find(field)
            if field_element is not None:
                field_value = field_element.text
            else:
                field_value = ""
            values[field.split("/")[-1]] = field_value

        # format the output line using the user-specified format string
        output_line = output_format.format(**values)

        # write the formatted output line to the output text file
        file.write(output_line + "\n")

# print a message indicating that the extraction is complete
print(f"Extraction complete. Results written to {output_file}.")
