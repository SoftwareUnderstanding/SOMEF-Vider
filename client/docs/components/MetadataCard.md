# Metadata Card

**Author:** Vitoriox

This is the component in with the metadata extracted from SOMEF will be displayed. That is why is the
biggest and most important component of all the webapp.

Inside the metadata card it will be used the following components: 
 - MetadataCardHeader
 - MetadataCardPanel
 - FilterDialog

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
| `showFilterDialog`       | `Boolean` | false                                                                                                | Flag that opens/closes the dialog for the filters                                                                                                                                                                                                                                                             |
| `header`                 | `Object`  | {}                                                                                                   | Object representation of the elements that must appear at the header of the metadata card                                                                                                                                                                                                                     |

## Methods

### mapMetadataFields()

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

This function return List of panelItems for each metadata field received. That list is formed by objects of this format:

    {
    excerpt: (Any),  // Content of the panel, the content can be any data type
    confidence: (Number), // Confidence given by somef
    extractionMethod: (String), // Extracction method used by somef to get this metadata
    }
**Syntax**

```typescript
buildPanelItem(name, somefItem)(): Object
```

### parseCitation()
Given a String input in bibtex notation, this method returns the HTML equivalent for that citation.

**Syntax**

```typescript
parseCitation(data)(): String (HTML format)
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