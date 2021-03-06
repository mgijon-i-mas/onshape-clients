/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class BTDocumentSearchParams {
    'type'?: string;
    'rawQuery'?: string;
    'offset'?: number;
    'limit'?: number;
    'ownerId'?: string;
    'parentId'?: string;
    'documentFilter'?: number;
    'sortColumn'?: string;
    'sortOrder'?: string;
    'foundIn'?: BTDocumentSearchParams.FoundInEnum;
    'when'?: BTDocumentSearchParams.WhenEnum;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "type",
            "type": "string"
        },
        {
            "name": "rawQuery",
            "baseName": "rawQuery",
            "type": "string"
        },
        {
            "name": "offset",
            "baseName": "offset",
            "type": "number"
        },
        {
            "name": "limit",
            "baseName": "limit",
            "type": "number"
        },
        {
            "name": "ownerId",
            "baseName": "ownerId",
            "type": "string"
        },
        {
            "name": "parentId",
            "baseName": "parentId",
            "type": "string"
        },
        {
            "name": "documentFilter",
            "baseName": "documentFilter",
            "type": "number"
        },
        {
            "name": "sortColumn",
            "baseName": "sortColumn",
            "type": "string"
        },
        {
            "name": "sortOrder",
            "baseName": "sortOrder",
            "type": "string"
        },
        {
            "name": "foundIn",
            "baseName": "foundIn",
            "type": "BTDocumentSearchParams.FoundInEnum"
        },
        {
            "name": "when",
            "baseName": "when",
            "type": "BTDocumentSearchParams.WhenEnum"
        }    ];

    static getAttributeTypeMap() {
        return BTDocumentSearchParams.attributeTypeMap;
    }
}

export namespace BTDocumentSearchParams {
    export enum FoundInEnum {
        ALL = <any> 'ALL',
        WORKSPACES = <any> 'WORKSPACES',
        VERSIONS = <any> 'VERSIONS'
    }
    export enum WhenEnum {
        ALL = <any> 'ALL',
        LATEST = <any> 'LATEST',
        LATESTPERHIT = <any> 'LATEST_PER_HIT'
    }
}
