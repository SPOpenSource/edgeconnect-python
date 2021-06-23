# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# template : ECOS configuration templates


def get_all_template_groups(self) -> dict:
    """Get all template groups

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/templateGroups

    :return: Returns dictionary of all template groups
    :rtype: dict
    """
    return self._get("/template/templateGroups")


def get_template_group(
    self,
    template_group: str,
) -> dict:
    """Get template group by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/templateGroups/{templateGroup}

    :param template_group: Name of template group,
        e.g. ``Default Template Group``
    :type template_group: str
    :return: Returns dictionary of template group
    :rtype: dict
    """
    template_group.replace(" ", "%20")
    return self._get("/template/templateGroups/{}".format(template_group))


def post_template_group(
    self,
    template_group: str,
    template_group_body: dict,
) -> bool:
    """Update template group by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - POST
          - /template/templateGroups/{templateGroup}

    :param template_group: Name of template group,
        e.g. ``Default Template Group``
    :type template_group: str
    :param template_group_body: Nested dictionary of template group
        details\n
        * keyword **name** (`str`): Name of template group
        * keyword **templates** (`list[dict]`): List of template detail
          dictionaries \n
            * keyword **name** (`str`): Name of template
            * keyword **valObject** (`dict`): Template details
    :type template_group_body: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    # template_group_body:
    #   TemplateCreateBody {
    #       name (string),
    #      templates (array[TemplatePOST]): An array of the templates to
    #                                       create/update
    #   }

    # where templates is a list of Template objects:
    #   Template {
    #       name (string, optional): The name of the template. See the
    #                                default template group for all the
    #                                names of the templates
    #       valObject (object, optional): The template data to configure
    #   }

    template_group.replace(" ", "%20")
    return self._post(
        "/template/templateGroups/{}".format(template_group),
        data=template_group_body,
        return_type="bool",
    )


def delete_template_group(
    self,
    template_group: str,
) -> bool:
    """Delete specified template group

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - DELETE
          - /template/templateGroups/{templateGroup}

    :param template_group: Name of template group,
        e.g. ``Default Template Group``
    :type template_group: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    template_group.replace(" ", "%20")
    return self._delete(
        "/template/templateGroups/{}".format(template_group),
        expected_status=[204],
        return_type="bool",
    )


def create_template_group(
    self,
    template_group_body: dict,
) -> bool:
    """Create new template group.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - POST
          - /template/templateCreate

    .. note::
        If group does not yet exist, the first post will not include
        selected templates (return of HTTP 204 instead of 200)

    :param template_group_body: Nested dictionary of template group
        details\n
        * keyword **name** (`str`): Name of template group
        * keyword **templates** (`list[dict]`): List of template detail
          dictionaries \n
            * keyword **name** (`str`): Name of template
            * keyword **valObject** (`dict`): Template details
    :type template_group_body: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    # template_group_body:
    #   TemplateCreateBody {
    #       name (string),
    #      templates (array[TemplatePOST]): An array of the templates
    #                                       to create/update
    #   }

    # where templates is a list of Template objects:
    #   Template {
    #       name (string, optional): The name of the template. See the
    #                                default template group for all the
    #                                names of the templates
    #       valObject (object, optional): The template data to configure
    #   }

    return self._post(
        "/template/templateCreate",
        expected_status=[200, 204],
        data=template_group_body,
        return_type="bool",
    )


def get_selected_templates_in_template_group(
    self,
    template_group: str,
) -> list:
    """Get selected templates for specified template group

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/templateSelection/{templateGroup}

    :param template_group: Name of template group,
        e.g. ``Default Template Group``
    :type template_group: str
    :return: Returns list of selected templates
    :rtype: list
    """
    template_group.replace(" ", "%20")
    return self._get("/template/templateSelection/{}".format(template_group))


def select_templates_for_template_group(
    self,
    template_group: str,
    selected_templates: list[str],
) -> bool:
    """Select template(s) for use in template group

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - POST
          - /template/templateSelection/{templateGroup}

    :param template_group: Name of template group,
        e.g. ``Default Template Group``
    :type template_group: str
    :param selected_templates: List of templates by name to be selected
        for the template group
    :type selected_templates: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    template_group.replace(" ", "%20")
    return self._post(
        "/template/templateSelection/{}".format(template_group),
        data=selected_templates,
        return_type="bool",
    )


def get_appliance_template_history(
    self,
    ne_pk: str,
    latest: bool,
) -> list:
    """Get history of applied templates to the specified appliance. Will
    return a HTTP 204 if no data available.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/history/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param latest: ``True`` for latest applied templates only, or
        ``False`` for all
    :type latest: str
    :return: Returns list of applied templates
    :rtype: list
    """
    return self._get(
        "/template/history/{}?latestOnly={}".format(ne_pk, latest),
        expected_status=[200, 204],
    )


def get_appliance_applied_template_goups(
    self,
    ne_pk: str,
) -> list:
    """Get applied template groups to specified appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/history/groupList/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns list of applied templates
    :rtype: list
    """
    return self._get("/template/history/groupList/{}".format(ne_pk))


def get_template_group_association_all_appliances(self) -> dict:
    """Get complete association map of appliances to template groups

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/applianceAssociation/

    :return: Returns dictionary of appliances and associated template
        groups \n
        * keyword **<appliance_ne_pk>** (`list[str]`): List of applied
          template groups
    :rtype: dict
    """
    return self._get("/template/applianceAssociation")


def get_appliance_template_groups_association(
    self,
    ne_pk: str,
) -> dict:
    """Get association map of appliance to template groups

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/applianceAssociation/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance and associated template
        groups \n
        * keyword **templateIds** (`list[str]`): List of applied
          template groups
    :rtype: dict
    """
    return self._get("/template/applianceAssociation/{}".format(ne_pk))


def associate_template_group_to_appliance(
    self,
    ne_pk: str,
    template_groups_list: list[str],
) -> dict:
    """
    Associate list of template groups to specified appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - POST
          - /template/applianceAssociation/{nePk}

    .. warning::
        The list of templates posted will be the complete association
        for the appliance. To add a tempalte group to existing
        associated templates, include existing template groups. Use
        :func:`~silverpeak_python_sdk.Orchestrator.get_appliance_template_groups_association`
        to retrieve current associated template groups to an appliance.

    **Example**: If you want to add the template group "NEW-TEMPLATE"
    to the appliance with an NePK of "10.NE" and the appliance is
    already associated with the template group "EXISTING-TEMPLATE"
    you would pass the following:

    .. code-block:: python

        Orchestrator.associate_template_group_to_appliance(
            ne_pk = "10.NE",
            template_groups_list = ["EXISTING-TEMPLATE","NEW-TEMPLATE"],
        )

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param template_groups_list: List of template groups by name to
        associate to appliance
    :type template_groups_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: E501, W505
    data = {"templateIds": template_groups_list}

    return self._post(
        "/template/applianceAssociation/{}".format(ne_pk),
        data=data,
        return_type="bool",
    )


def get_template_groups_priorities(self) -> dict:
    """Get order that template groups will be applied in

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - GET
          - /template/templateGroupPriorities

    :return: Returns dictionary of appliance and associated template
        groups \n
        * keyword **priorities** (`list[str]`): List of applied template
          groups
    :rtype: dict
    """
    return self._get("/template/templateGroupsPriorities")


def set_template_groups_priorities(
    self,
    template_groups_list: list[str],
) -> dict:
    """Set order that template groups will be applied in

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - template
          - POST
          - /template/templateGroupPriorities

    :param template_groups_list: Ordered list of template groups by name
        to be specified for prioirty
    :type template_groups_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"templateIds": template_groups_list}

    return self._get(
        "/template/templateGroupsPriorities",
        data=data,
        return_type="bool",
    )
