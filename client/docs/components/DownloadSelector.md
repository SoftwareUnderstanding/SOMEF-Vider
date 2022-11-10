# Download Selector

**Author:** Vitoriox
This is a small component that shows a list of available download sources for the metadata extracted and emits to the
parent component the filetype selected

```html
    <download-selector @download="download"/>
```

## Data

| Name             | Type      | Initial value                                                                                        | Description                                                             |
|------------------|-----------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `downloadTypes`  | `Array`   | [{text:'JSON', value:'json'},{text:'CodeMeta', value: 'codemeta'},{text:'Turtle', value: 'turtle'},] | List that contains an object for every option for the download selector |
| `toggleSelector` | `Boolean` | false                                                                                                | Flag that opens/closes the download selector                            |

## Methods

### changeHandler()
This method emits the `download` event with the String of the filetype given at the input.
It is used to notify the main component that the user wants to download the metadata file and the extension of it. 

**Syntax**

```typescript
changeHandler(fileType)(): void
```
