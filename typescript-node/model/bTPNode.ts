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

import { BTConnection } from './bTConnection';
import { BTObjectId } from './bTObjectId';
import { BTPSpace } from './bTPSpace';

export class BTPNode {
    'shortDescriptor'?: string;
    'atomic'?: boolean;
    'startSourceLocation'?: number;
    'endSourceLocation'?: number;
    'documentationType'?: BTPNode.DocumentationTypeEnum;
    'spaceBefore'?: BTPSpace;
    'changeableChildFieldIndices'?: Array<number>;
    'firstChildField'?: number;
    'spaceAfter'?: BTPSpace;
    'spaceDefault'?: boolean;
    'nodeId'?: string;
    'childMapIndices'?: Array<number>;
    'atomicChildIndices'?: Array<number>;
    'nodeIdRaw'?: BTObjectId;
    'childListIndices'?: Array<number>;
    'typeId'?: number;
    'exportTypeName'?: string;
    'connectionSource'?: BTConnection;
    'unknownClass'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "shortDescriptor",
            "baseName": "shortDescriptor",
            "type": "string"
        },
        {
            "name": "atomic",
            "baseName": "atomic",
            "type": "boolean"
        },
        {
            "name": "startSourceLocation",
            "baseName": "startSourceLocation",
            "type": "number"
        },
        {
            "name": "endSourceLocation",
            "baseName": "endSourceLocation",
            "type": "number"
        },
        {
            "name": "documentationType",
            "baseName": "documentationType",
            "type": "BTPNode.DocumentationTypeEnum"
        },
        {
            "name": "spaceBefore",
            "baseName": "spaceBefore",
            "type": "BTPSpace"
        },
        {
            "name": "changeableChildFieldIndices",
            "baseName": "changeableChildFieldIndices",
            "type": "Array<number>"
        },
        {
            "name": "firstChildField",
            "baseName": "firstChildField",
            "type": "number"
        },
        {
            "name": "spaceAfter",
            "baseName": "spaceAfter",
            "type": "BTPSpace"
        },
        {
            "name": "spaceDefault",
            "baseName": "spaceDefault",
            "type": "boolean"
        },
        {
            "name": "nodeId",
            "baseName": "nodeId",
            "type": "string"
        },
        {
            "name": "childMapIndices",
            "baseName": "childMapIndices",
            "type": "Array<number>"
        },
        {
            "name": "atomicChildIndices",
            "baseName": "atomicChildIndices",
            "type": "Array<number>"
        },
        {
            "name": "nodeIdRaw",
            "baseName": "nodeIdRaw",
            "type": "BTObjectId"
        },
        {
            "name": "childListIndices",
            "baseName": "childListIndices",
            "type": "Array<number>"
        },
        {
            "name": "typeId",
            "baseName": "typeId",
            "type": "number"
        },
        {
            "name": "exportTypeName",
            "baseName": "exportTypeName",
            "type": "string"
        },
        {
            "name": "connectionSource",
            "baseName": "connectionSource",
            "type": "BTConnection"
        },
        {
            "name": "unknownClass",
            "baseName": "unknownClass",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTPNode.attributeTypeMap;
    }
}

export namespace BTPNode {
    export enum DocumentationTypeEnum {
        FUNCTION = <any> 'FUNCTION',
        PREDICATE = <any> 'PREDICATE',
        CONSTANT = <any> 'CONSTANT',
        ENUM = <any> 'ENUM',
        USERTYPE = <any> 'USER_TYPE',
        FEATUREDEFINITION = <any> 'FEATURE_DEFINITION',
        FILEHEADER = <any> 'FILE_HEADER',
        UNDOCUMENTABLE = <any> 'UNDOCUMENTABLE',
        UNKNOWN = <any> 'UNKNOWN'
    }
}
