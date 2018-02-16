// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package types

import (
	"gopkg.in/validator.v2"
)

type Link struct {
	Destdir  int32        `json:"destdir" validate:"nonzero"`
	Destname int32        `json:"destname" validate:"nonzero"`
	Moddate  int32        `json:"moddate" validate:"nonzero"`
	Name     string       `json:"name" validate:"nonzero"`
	Type     EnumLinkType `json:"type" validate:"nonzero"`
}

func (s Link) Validate() error {

	return validator.Validate(s)
}
