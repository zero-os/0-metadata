// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package types

import (
	"gopkg.in/validator.v2"
)

type Dir struct {
	Acl           int32          `json:"acl" validate:"nonzero"`
	BobjectItems  []Link_bobject `json:"bobjectItems" validate:"nonzero"`
	Files         []string       `json:"files" validate:"nonzero"`
	LinkItems     []Link         `json:"linkItems" validate:"nonzero"`
	MetadataItems []Metadata     `json:"metadataItems" validate:"nonzero"`
	Name          string         `json:"name" validate:"nonzero"`
	Posix         Posix          `json:"posix,omitempty"`
	Secret        string         `json:"secret" validate:"nonzero"`
	Size          int32          `json:"size" validate:"nonzero"`
	SpecialItems  []Special      `json:"specialItems" validate:"nonzero"`
	Subdirs       []Link         `json:"subdirs" validate:"nonzero"`
	Uid           int32          `json:"uid" validate:"nonzero"`
	UidParent     int32          `json:"uidParent" validate:"nonzero"`
}

func (s Dir) Validate() error {

	return validator.Validate(s)
}