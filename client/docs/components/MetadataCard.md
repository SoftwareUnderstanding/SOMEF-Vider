# Metadata Card

**Author:** Vitoriox

This is the component in with the metadata extracted from SOMEF will be displayed. That is why is the
biggest and most important component of all the webapp.

Inside the metadata card it will be used the following components: 
 - ConfidenceChip
 - ExtractMethodChip
 - LastModifyChip
 - FilterDialog

This component HTML is divided into 2 main sections:
 - **Header:** The header is a rather complex v-card which contains the most relevant information of the repository
    analized such as description, license, title, icon, etc. If some metadata that must be in the header could 
    not be extracted, it will show (*NO DATA AVAILABLE*) on that field.
 - **Body:** This is where the rest of the fields are displayed, grows or shrinks depending on the number of metadata
    fields extracted. Depending on the type of object that is contained in the metadata field, the v-expansion-panel 
    will have a different configuration:
   - If the content is an array, the expansion panel will contain a v-carousel component to show all the content of 
    array
   - If the content is not an array, the expansion panel will display the excerpt field as it is given by SOMEF. 
   Except the *Citation* field, this field must be processed by the parseCitation() function before displaying it.
```html
    <metadata-card
        :threshold="threshold"
        :metadata="metadata"
        @click-download="chilDownload"
    ></metadata-card>
```

## Props

| Name                   | Type     | Default | Description                                                                                                  |
|------------------------|----------|---------|--------------------------------------------------------------------------------------------------------------|
| `threshold` *required* | `Number` | 0       | Threshold value given by the user in the form. It's required to show properly the ConfidenceChip components. |
| `metadata` *required*  | `Objec`  | {}      | JSON Object returned by SOMEF, here is where all the metadata is contained                                   |


## Data

| Name                     | Type      | Initial value                                                                                        | Description                                                                                                                                                                                                                                                                                                   |
|--------------------------|-----------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tabIndex`               | `Number`  | null                                                                                                 | Represents the index of the metadata field selected at the tab menu selector                                                                                                                                                                                                                                  |
| `panelItemsList`         | `Array`   | []                                                                                                   | List of the panelItems to be displayed in the body. A panel item is the standardized representation of a metadata field. Every panelItem must follow the same object structure `panelItem={name:"String", body:[subPanelItem1, subPanelItem2, ...], confidence: "Number", extractionMethods: "Set[Strings]"}` |
| `downloadFiletypesList`  | `Array`   | [{text:'JSON', value:'json'},{text:'CodeMeta', value: 'codemeta'},{text:'Turtle', value: 'turtle'},] | List that contains an object for every option for the download selector                                                                                                                                                                                                                                       |
| `toggleDownloadSelector` | `Boolean` | false                                                                                                | Flag that opens/closes the download selector                                                                                                                                                                                                                                                                  |
| `showFilterDialog`       | `Boolean` | false                                                                                                | Flag that opens/closes the dialog for the filters                                                                                                                                                                                                                                                             |
| `header`                 | `Object`  | {}                                                                                                   | Object representation of the elements that must appear at the header of the metadata card                                                                                                                                                                                                                     |

## Methods

### generateTabs()

This method receive the JSON object with the metadata returned by SOMEF. Does not have output, but it 
initialises the two main parts of the metadata card (the header and the body) calling other methods

**Syntax**

```typescript
generateTabs(rawMetadata): void
```

### buildHeaderItem()
This method receive as an input the name of the header field and the metadata content associated to it. It is responsible
for initializing the `header` data variable.

This method will process the input different depending on the type of header field to be initialized

**Syntax**

```typescript
buildHeaderItem(name, somefItem)(): void
```

### buildPanelItem()
This method is similar to `buildHeaderItem`. Receives the name of the field name and de metadata object associated to build
the respective panel. It is responsible for initialize the `panelItemsList` data variable.

All the panel item objects generated by this method has this form:

    name: (String), // Name of the panel, it is the same as the input name
    body: (Array),  // Content of the panel, the content can be any data type, including another panel item objects
    confidence: (Number), // Confidence given by somef, only used if the body is NOT a list of panel items
    extractionMethods: (Set), // List of all the extracction methods used by somef to get this metadata

**Syntax**

```typescript
buildPanelItem(name, somefItem)(): void
```

### isHeaderItem()
Determines if a given field name is part of the header or not.
It uses the `METADATA_FIELDS_FOR_HEADER` constant as a list for comparison.
If the name of the field apears in that list, that means is part of the header, otherwise return false.

**Syntax**

```typescript
isHeaderItem(name)(): Boolean
```

### parseCitation()
Given a String input in bibtex notation, this method returns the HTML equivalent for that citation.

**Syntax**

```typescript
parseCitation(data)(): String (HTML format)
```

### downloadMetadata()
This method emits the `click-download` event with the String of the filetype given at the input.
It is used to notify the main component that the user wants to download the metadata file and the extension of it. 

**Syntax**

```typescript
downloadMetadata(fileType)(): void
```

### stringToTitleCase()
Converts any input string to the TitleCase format

**Syntax**

```typescript
stringToTitleCase(str)(): String
```

### excerptToString()
Converts the input excerpt to String. The excerpt is given by somef and can be any data type (Object, Array, String)

**Syntax**

```typescript
excerptToString(excerpt)(): String
```